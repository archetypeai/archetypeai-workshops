# archetypeai-workshops

Hands-on workshops for building with Newton, Archetype AI's physical world model. Each workshop is a self-contained Jupyter notebook that runs in Google Colab: no GPU, no local models, only an API key.

## Workshops

| Workshop | What you build | Time | Open |
|---|---|---|---|
| [Vision](vision_workshop/) | From a video of a manual task to a PASS / FAIL inspection, an activity timeline, bounding boxes and a written shift note. | 90 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archetypeai/archetypeai-workshops/blob/main/vision_workshop/newton_vision_workshop.ipynb) |
| Time series | Coming soon | | |

## Before you start

1. **An Archetype AI account and API key.** Log in at https://platform.u1.archetypeai.app/console/profile and create a key on the Profile & API Keys page. No account yet? Request one at https://www.archetypeai.io/try-newton.
2. **Somewhere to run a notebook.** Google Colab needs nothing installed. Locally, Python 3.10 or later and `pip install archetypeai opencv-python-headless matplotlib pandas jupyter`.
3. **About an hour and a half** per workshop.

## How a workshop works

Open the participant notebook in Colab: click its **Open in Colab** badge, or go to https://colab.research.google.com/#create=true&upload=true (File → Upload notebook) and upload the `.ipynb` file. Paste your key into the setup cell and run the cells in order. Cells marked **Exercise** are yours to write; each has a hint and a checkpoint that says what a correct result looks like. A solution notebook sits next to every participant notebook: try the exercise first, then compare.

## Repository layout

```
vision_workshop/        the vision workshop: participant and solution notebooks
timeseries_workshop/    the time-series workshop (in preparation)
```

## Learn more

- Documentation: https://docs.archetypeai.app
- Example projects: https://github.com/archetypeai
- Agent skills for coding assistants: https://github.com/archetypeai/agent-skills

## License

Apache 2.0, see [LICENSE](LICENSE). The sample recordings used in the workshops were produced by Archetype AI for this purpose.
