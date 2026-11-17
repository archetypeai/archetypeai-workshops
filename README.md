# archetypeai-workshops

Hands-on workshops for building with Newton, Archetype AI's physical world model. Each workshop is a self-contained Jupyter notebook that runs in Google Colab: no GPU, no local models, only an API key.

## Workshops

| Workshop | What you build | Time | Open |
|---|---|---|---|
| [Vision](vision_workshop/) | From a video of a manual task to a PASS / FAIL inspection, an activity timeline, bounding boxes and a written shift note. | 90 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archetypeai/archetypeai-workshops/blob/main/vision_workshop/newton_vision_workshop.ipynb) |
| [Time series](timeseries_workshop/) | From a CSV file of sensor readings to Newton embeddings, a 2-D map of a machine's states, a classifier that names the state from a few labelled examples and a state timeline. | 90 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archetypeai/archetypeai-workshops/blob/main/timeseries_workshop/newton_timeseries_workshop.ipynb) |

## Before you start

1. **An Archetype AI account and API key.** Log in at https://platform.u1.archetypeai.app/console/profile and create a key on the Profile & API Keys page. No account yet? Request one at https://www.archetypeai.io/try-newton.
2. **Somewhere to run a notebook.** Google Colab needs nothing installed. Locally, Python 3.10 or later and `pip install archetypeai opencv-python-headless numpy pandas matplotlib scikit-learn jupyter`.
3. **About an hour and a half** per workshop.

## How a workshop works

Open the participant notebook in Colab: click its **Open in Colab** badge, or go to https://colab.research.google.com/#create=true&upload=true (File → Upload notebook) and upload the `.ipynb` file. Paste your key into the setup cell and run the cells in order. Cells marked **Exercise** are yours to write; each has a hint and a checkpoint that says what a correct result looks like. A solution notebook sits next to every participant notebook: try the exercise first, then compare.

## Repository layout

```
vision_workshop/        the vision workshop: participant and solution notebooks
timeseries_workshop/    the time-series workshop: participant and solution notebooks
tools/                  the script that builds the time-series solution notebooks
```

## Learn more

- Documentation: https://docs.archetypeai.app
- Example projects: https://github.com/archetypeai
- Agent skills for coding assistants: https://github.com/archetypeai/agent-skills

## License

Apache 2.0, see [LICENSE](LICENSE). The sample videos used in the vision workshop were produced by Archetype AI for this purpose. The drilling log used in the time-series workshop comes from the [Volve field dataset](https://www.equinor.com/energy/volve-data-sharing), disclosed by Equinor and its Volve licence partners for research, study and development, and is used under the Equinor Open Data Licence.
