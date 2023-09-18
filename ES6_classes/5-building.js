export default class Building {
  constructor(sqft) {
    if (
      this.evacuationWarningMessage === undefined &&
      this.constructor !== Building
    ) {
      throw new Error(
        "Class extending Building must override evacuationWarningMessage"
      );
    }
    this._sqft = sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }

  get sqft() {
    return this._sqft;
  }
}
