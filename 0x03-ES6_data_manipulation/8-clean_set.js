/* eslint-disable no-unused-vars */
function cleanSet(set, startString) {
  let cleanString = '';
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      cleanString += `${value.slice(startString.length)}-`;
    }
  });
  return cleanString.slice(0, -1);
}
