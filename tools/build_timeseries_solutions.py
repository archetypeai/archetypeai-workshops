"""Build the solution notebooks of the time-series workshop from the participant notebook.

The participant notebook is the single source. This script copies it, replaces each exercise
with its solution, and writes:

    timeseries_workshop/newton_timeseries_workshop_SOLUTION.ipynb            no outputs
    timeseries_workshop/newton_timeseries_workshop_SOLUTION_executed.ipynb   run top to bottom (--execute)

Run it from the repository root whenever the participant notebook changes, in the Python
environment used to run the workshop locally (see timeseries_workshop/README.md):

    python tools/build_timeseries_solutions.py --execute

--execute runs the solution notebook in that environment's `python3` kernel. It calls the
Archetype AI API (about 90 requests) and needs ATAI_API_KEY in the environment.
--clean-copy PATH also writes the participant notebook itself without outputs, for committing.

The script stops with an error if an exercise has no solution here, or a solution here matches
no exercise.
"""
import argparse
import copy
import pathlib
import re
import sys

import nbformat

FOLDER = pathlib.Path("timeseries_workshop")
PARTICIPANT = FOLDER / "newton_timeseries_workshop.ipynb"
SOLUTION = FOLDER / "newton_timeseries_workshop_SOLUTION.ipynb"
EXECUTED = FOLDER / "newton_timeseries_workshop_SOLUTION_executed.ipynb"

# The metadata the published notebooks carry: a generic kernel name and the Colab settings, as in the vision workshop.
METADATA = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
            "colab": {"provenance": [], "toc_visible": True}}

STUB = "# ===== YOUR CODE HERE ====="                       # an exercise cell that holds only guidance comments
BLOCK = re.compile(r"^[ \t]*# ===== YOUR CODE HERE.*?# ===== END OF YOUR CODE =====[ \t]*\n", re.S | re.M)   # guidance inside a written cell

# One solution per exercise, keyed by the number in its "### Exercise N.M" heading.
SOLUTIONS = {
    "1.1": '''\
for size in (16, 32, 64, 128):
    n = len(log) // size                                                              # whole windows that fit
    mixed = sum(len(set(state[i * size:(i + 1) * size])) > 1 for i in range(n))       # windows that hold more than one state
    print(f"{size:4d} readings: {n:4d} windows, {mixed} mixed")''',

    "2.1": '''\
for how in ("recording", "window"):
    levels = scale(windows, how).mean(axis=2)          # [windows x channels]: each window's level on each channel
    share = levels.var(axis=0)                         # how much the level varies between windows, per channel
    print(f"{how:10s}", dict(zip(CHANNELS, share.round(2).tolist())))''',

    # Exercise 3.1 fills in the first four lines of show_similarity; the rest of that cell is kept.
    "3.1": '''\
    similarity = vectors @ vectors.T                                    # [windows x windows]; for vectors of length 1 this is the cosine similarity
    same_state = window_state[:, None] == window_state[None, :]         # True where the row's window and the column's window have the same state
    not_itself = ~np.eye(len(vectors), dtype=bool)                      # a window compared with itself always scores 1: leave those out
    within, between = similarity[same_state & not_itself].mean(), similarity[~same_state].mean()
''',

    "4.1": '''\
for perplexity in (5, 30):
    draw_map(project(vectors, perplexity), f"perplexity {perplexity}")''',

    "5.1": '''\
for per_state in (1, 2, 3, 5):
    scores = []
    for seed in range(20):
        picked = pick_examples(per_state, seed)
        scores.append(accuracy(classify(vectors, picked), picked))
    print(f"{per_state} per state: average accuracy {np.mean(scores):.3f}, worst of 20 picks {np.min(scores):.3f}")''',
}


def without_outputs(nb):
    """A copy of the notebook with no outputs and no run numbers, carrying the published metadata."""
    clean = copy.deepcopy(nb)
    for cell in clean.cells:
        if cell.cell_type == "code":
            cell.outputs, cell.execution_count = [], None
    clean.metadata = nbformat.from_dict(METADATA)
    return clean


def with_solutions(nb):
    """A copy of the notebook in which every exercise cell holds its solution."""
    solved = without_outputs(nb)
    exercise, used = None, []
    for cell in solved.cells:
        heading = re.match(r"### Exercise (\d+\.\d+)", cell.source)
        if cell.cell_type == "markdown" and heading:
            exercise = heading.group(1)
        if cell.cell_type != "code" or "YOUR CODE HERE" not in cell.source:
            continue
        if exercise not in SOLUTIONS:
            sys.exit(f"Exercise {exercise} has no solution in this script.")
        if cell.source.startswith(STUB):
            cell.source = SOLUTIONS[exercise]
        else:
            cell.source, replaced = BLOCK.subn(lambda _: SOLUTIONS[exercise], cell.source)
            if replaced != 1:
                sys.exit(f"Exercise {exercise}: expected one marked block in its cell, found {replaced}.")
        used.append(exercise)
    unused = sorted(set(SOLUTIONS) - set(used))
    if unused or len(used) != len(set(used)):
        sys.exit(f"Solutions without a matching exercise cell: {unused}; exercises found: {used}.")
    return solved, used


def executed_copy(nb):
    """Run the notebook top to bottom and return it with its outputs.
    The outputs of the install cell and of the key cell are removed: the first is noise, the second shows part of the API key."""
    from nbclient import NotebookClient
    run = copy.deepcopy(nb)
    NotebookClient(run, timeout=900, kernel_name="python3", resources={"metadata": {"path": str(FOLDER)}}).execute()
    for cell in run.cells:
        if cell.cell_type == "code" and (cell.source.startswith("%pip") or "getpass" in cell.source):
            cell.outputs = []
    run.metadata = nbformat.from_dict({**METADATA, "language_info": run.metadata.get("language_info", METADATA["language_info"])})
    if any("Key loaded" in str(cell.get("outputs")) for cell in run.cells):
        sys.exit("An output still shows the API key line; nothing was written.")
    return run


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--execute", action="store_true", help="also run the solution notebook and write the executed copy")
    parser.add_argument("--clean-copy", metavar="PATH", help="also write the participant notebook without outputs to PATH")
    args = parser.parse_args()

    participant = nbformat.read(PARTICIPANT, as_version=4)
    solved, used = with_solutions(participant)
    nbformat.validate(solved)
    nbformat.write(solved, SOLUTION)
    print(f"{SOLUTION}: {len(solved.cells)} cells, solutions for exercises {', '.join(used)}")

    if args.clean_copy:
        clean = without_outputs(participant)
        nbformat.validate(clean)
        nbformat.write(clean, args.clean_copy)
        print(f"{args.clean_copy}: the participant notebook without outputs")

    if args.execute:
        run = executed_copy(solved)
        nbformat.validate(run)
        nbformat.write(run, EXECUTED)
        code = [cell for cell in run.cells if cell.cell_type == "code"]
        print(f"{EXECUTED}: {len(code)} code cells run, {sum(bool(cell.outputs) for cell in code)} with outputs")


if __name__ == "__main__":
    main()
