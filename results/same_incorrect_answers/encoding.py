import chardet

def detect_encoding(file_path):
  """
  Detects the encoding of a file using chardet library.

  Args:
      file_path (str): Path to the file.

  Returns:
      str: The detected encoding or None if detection fails.
  """
  with open(file_path, 'rb') as f:
    rawdata = f.read()
  return chardet.detect(rawdata)['encoding']

# Example usage
file_path = "llama-instruct/Meta-Llama-3-8B-Instruct_same_incorrect_answer_1.txt"
encoding = detect_encoding(file_path)

if encoding:
  print(f"Detected encoding: {encoding}")
else:
  print("Encoding detection failed.")
