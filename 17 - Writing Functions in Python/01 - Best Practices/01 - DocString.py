# Add a docstring to count_letter()
def count_letter(content, letter):
  """
    Count the number of times `letter` appears in `content`.

    Parameters:
        content (str): The string in which you want to count occurrences.
        letter (str): The character you want to count.

    Returns:
        int: The number of times `letter` appears in `content`.

    Raises:
        ValueError: If `letter` is not a single character string.
    """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


