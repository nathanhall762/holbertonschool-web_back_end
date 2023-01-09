export default function returnHowManyArguments(...args) {
  let n = 0;
  for (const arg in args) {
    if (arg) {
      n += 1;
    }
  }
  return n;
}
