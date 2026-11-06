# Vision workshop: from a video to a work log

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archetypeai/archetypeai-workshops/blob/main/vision_workshop/newton_vision_workshop.ipynb)

Starting from an ordinary video of a worker assembling parts, you use Newton to produce:

1. a plain-English description of video frames,
2. structured JSON answers a downstream program can use,
3. a PASS / FAIL inspection of a whole video,
4. a second-by-second activity timeline,
5. bounding boxes around objects, drawn from Newton's answer,
6. a before / after comparison,
7. a written shift note, in English and Japanese.

The last section runs the same pipeline on a video you upload.

| File | Use |
|---|---|
| `newton_vision_workshop.ipynb` | the workshop: run the cells in order and write the eight exercise cells |
| `newton_vision_workshop_SOLUTION.ipynb` | the same notebook with every cell filled in |
| `newton_vision_workshop_SOLUTION_executed.ipynb` | the solution as run end to end, with Newton's answers, the timeline and the bounding boxes shown; read it on GitHub or download it to see the results without an API key |

## Running it

**Google Colab.** Click the badge above, or open https://colab.research.google.com/#create=true&upload=true and upload `newton_vision_workshop.ipynb` (the same dialog is File → Upload notebook inside Colab). Paste your API key into the setup cell (section 1); if you leave it empty the cell prompts for it without showing it.

**Locally.** Python 3.10 or later: `pip install archetypeai opencv-python-headless matplotlib pandas jupyter`, then `jupyter notebook newton_vision_workshop.ipynb`.

The sample clips (a 31-second assembly task and a parcel delivery) download from inside the notebook.

## Agenda, 90 minutes

| Section | Topic |
|---|---|
| 0 to 1 | your API key, the setup, the first call |
| 2 to 3 | the sample video, one image and one question |
| 4 | structured JSON answers |
| 5 | a whole video in one call: PASS / FAIL inspection |
| 6 | an activity timeline, second by second |
| 7 | Newton finds objects: bounding boxes |
| 8 | before and after |
| 9 | from observations to a shift note, English and Japanese |
| 10 | your own video |
| 11 | what you built, and the limits to know before scaling up |

## Good to know

- Text calls take under a second, one image 1 to 3 s, a 32-frame video 3 to 6 s.
- Up to 16 images per multi-image call and 64 frames per video call.
- Several frames in one call need either `query_metadata` (frames of one clip) or `multi_image: true` (independent images).
- Keep your key out of the notebook before sharing it: the setup cell's placeholder is empty on purpose.
