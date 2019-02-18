def digital_root(n):
  stringed = str(n)
  total = 0
  for c in stringed:
    total += int(c)
  if total > 9:
    return digital_root(total)
  else:
    return total