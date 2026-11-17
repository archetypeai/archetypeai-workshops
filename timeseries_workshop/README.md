# Time-series workshop: from sensor readings to a state timeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archetypeai/archetypeai-workshops/blob/main/timeseries_workshop/newton_timeseries_workshop.ipynb)

Starting from a CSV file of sensor readings from a drilling rig, you use Newton to produce:

1. a plot of the raw signal, cut into windows (short, equal-length slices of the recording),
2. a Newton embedding for each window: a list of numbers that summarises how the signal behaves in it,
3. a 2-D map of the embeddings, where the rig's states show up as separate groups,
4. a classifier that names the rig's state from a handful of labelled windows,
5. a state timeline for the whole recording.

| File | Use |
|---|---|
| `newton_timeseries_workshop.ipynb` | the workshop: run the cells in order and write the five exercises |
| `newton_timeseries_workshop_SOLUTION.ipynb` | the same notebook with every cell filled in |
| `newton_timeseries_workshop_SOLUTION_executed.ipynb` | the solution as run end to end, with the plots, the map and the timeline shown; read it on GitHub or download it to see the results without an API key |

## Running it

**Google Colab.** Click the badge above, or open https://colab.research.google.com/#create=true&upload=true and upload `newton_timeseries_workshop.ipynb` (the same dialog is File → Upload notebook inside Colab). Paste your API key into the setup cell (section 1); if you leave it empty the cell prompts for it without showing it.

**Locally.** Python 3.10 or later: `pip install archetypeai numpy pandas matplotlib scikit-learn jupyter`, then `jupyter notebook newton_timeseries_workshop.ipynb`.

The sample data (a 3.8-hour drilling log from the [Volve field dataset](https://www.equinor.com/energy/volve-data-sharing): nine sensor channels and the rig's logged state) downloads from inside the notebook.

## Agenda, 90 minutes

| Section | Topic |
|---|---|
| 0 to 1 | your API key, the setup, the first call |
| 2 | the sample data: nine sensor channels and the rig's logged state |
| 3 | cut the recording into windows: length and overlap |
| 4 | scale the windows |
| 5 | a Newton embedding for every window, and how alike two windows are |
| 6 | a map of the embeddings |
| 7 | name the state from a few examples, and the state timeline |

## Good to know

- One request takes about a second. The 85 windows of the sample recording are sent 8 at a time and take about half a minute.
- A window is 16 to 1024 readings long, in a multiple of 16, and Newton returns one embedding of 768 numbers per channel.
- `OVERLAP` (section 3) and `SCALING` (section 4) are settings the later sections build on: change one and rerun the notebook from that cell down. Each window is one request, so an overlap of 0.75 means 340 requests instead of 85.
- Keep your key out of the notebook before sharing it: the setup cell's placeholder is empty on purpose.

## Rebuilding the solution notebooks

The two solution notebooks are generated from the participant notebook, so do not edit them by hand. After changing the participant notebook, run this from the repository root, in the environment described under **Locally** above and with your key exported as `ATAI_API_KEY`:

```
python tools/build_timeseries_solutions.py --execute
```

It fills in the five exercises from the solutions the script holds, then runs the result end to end: about 90 requests to Newton, a minute or two. Without `--execute` it writes only the unexecuted solution notebook and makes no requests.
