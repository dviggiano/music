# [WIP] Notation

Prototype for a music recommendation engine based purely on musical attributes.

## Getting started

### Installing FFmpeg

Because Notation uses Pydub, you'll need FFmpeg accessible from your system's PATH environment variable.

Find a compatible FFmpeg download [here](https://ffmpeg.org/download.html).

Then, add the location of the FFmpeg executable to your system's PATH environment variable. See
[here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiF8s7zytj_AhVolWoFHUMNAskQFnoECBEQAw&url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fdatabase%2Foracle%2F%2F%2F%2Fmachine-learning%2Foml4r%2F1.5.1%2Foread%2Fcreating-and-modifying-environment-variables-on-windows.html&usg=AOvVaw1GidrJ7uRZrEG57xTy4UB6&opi=89978449) for instructions.

### Running the app

Create a virtual environment (recommended):

```
python3 -m venv venv
```

Activate it on Windows:

```
venv\Scripts\activate
```

Or with Bash (Mac OS/Linux):

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Finally, run a development server:

```
flask run
```
You should then be able to interact with the API from your browser at `http://localhost:5000`.
