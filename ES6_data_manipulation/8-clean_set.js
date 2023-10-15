function cleanSet(set, startString) {
  const cleanedValues = [];

  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  for (const value of set) {
    if (value !== undefined && typeof startString === 'string' && value.startsWith(startString)) {
      cleanedValues.push(value.substring(startString.length));
    }
  }
  return cleanedValues.join('-');
}
