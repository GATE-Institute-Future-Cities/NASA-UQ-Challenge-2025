import os
import fire
from pathlib import Path

if __name__ == '__main__':
   fire.Fire(model)

def model(sample_index):
   # Copy the input file into the cwd
   command1 = "cp ./InputFiles/NASA_input_" + str(sample_index+1) + ".json ."
   exe_path = os.path.abspath(Path(__file__).parent / "local_model_windows.exe")
   command2 = os.system(f"{exe_path} NASA_input_{sample_index+1}.json")
   # Rename the output file
   command3 = "mv Y_out.csv Y_out_" + str(sample_index+1) + ".csv"

   #os.system(command1)
   os.system(command2)
   os.system(command3)

