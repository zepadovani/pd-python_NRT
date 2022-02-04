## Run PD patches in NRT using Python

The files in this repository demonstrate how to use Pure Data (Pd) patches designed to run in Non-Real-Time mode to batch-process (synthesize, analyze, etc) sounds in series using Python.

The `[pd_abs_NRT]` patch is designed to be opened and run by Pd from the command line (no GUI). A sine wave with a hanning envelope is synthesized, and is then written to a wave file. The objective, of course, is not exactly to generate a bunch of sinusoid audio files: the idea is rather of demonstrating how it is possible to pass arguments to a DSP algorithm and execute it in deferred time sequentially using python or some other script language.

The Pd patch itself can be run with the following command:

        pd -nogui -open teste_nrt.pd -send "nrt name teste.wav, freq 400, dur 3000"

(make sure the `pd` command is in your environment variables or modify the above command to the path where the pd binary is on your system)

The `run_50_times.py` and `run_50_times_multiprocessing.py` Python scripts demonstrate how you can create scripts to automate the process of running the above patch multiple times. In this case, generating 50 wave files with random values for the sinusoids frequency and duration.

To run:

        python run_50_times.py

or

        python run_50_times_multiprocessing.py

The other `.pd` files are auxiliary abstractions (that can be used to generate different types of windows).

Pd patches are vanilla (tested on Pd 0.52).

Tested on Python 3.9.7.

Hope it can be good start for your using case. :)

José Henrique Padovani, feb/2022
