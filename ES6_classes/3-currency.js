export default class Currency {
  constructor(code = "", name = "") {
    this._code = code;
    this._name = name;
  }

  set code(value) {
    this._code = value;
  }

  set name(value) {
    this._name = value;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
