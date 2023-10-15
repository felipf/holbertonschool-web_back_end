export default function cleanSet(set, startString) {
  const cleanValues = [];

  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const value of set) {
    if (
      value !== undefined &&
      typeof startString === 'string' &&
      value.startsWith(startString)
    ) {
      cleanValues.push(value.substrin(startString.length));
    }
  }
  return cleanValues.join('-');
}
