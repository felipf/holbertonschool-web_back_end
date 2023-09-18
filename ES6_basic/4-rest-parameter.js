export default function returnHowManyArguments(...args) {
  let sum = 0;
  args.forEach(() => {
    sum += 1;
  });
  return sum;
}
