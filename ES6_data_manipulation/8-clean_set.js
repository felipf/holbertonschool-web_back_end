export default function cleanSet(set, startString) {
  return new Set(
    [...set].filter(
      (item) => typeof item === 'string' && item.startsWith(startString)
    )
  );
}
