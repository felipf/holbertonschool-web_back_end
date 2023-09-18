export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(value) {
    this._amount = value;
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    this._currency = value;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    const code = this.currency._code;
    const name = this.currency._name;
    const money = `${this._amount} ${name} (${code})`;

    return money;
  }

  static convertPrice(amount = 0, conversionRate = 0) {
    if (typeof conversionRate !== "number") {
      throw new TypeError("conversionRate must be a number");
    }
    if (typeof amount !== "number") {
      throw new TypeError("amount must be a number");
    }
    return amount * conversionRate;
  }
}
