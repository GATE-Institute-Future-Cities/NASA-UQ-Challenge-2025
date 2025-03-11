def output_function(input=sample_index):
  # Postprocess the output files corresponding to the sample
  # number and extract the quantity of interest
  output_file_path = f'Y_out_{sample_index}.csv'
  df = pd.read_csv(output_file_path, header=None)
  return df