export default class Currency {
  constructor(code, name) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof code !== 'string') throw TypeError('Code must be a string');

    this._code = code;
    this._name = name;
  }

  /* getter name */
  get name() {
    return this._name;
  }

  /* setter name */
  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._name = value;
  }

  /* getter code */
  get code() {
    return this._code;
  }

  /* setter code */
  set code(value) {
    if (typeof value !== 'string') throw TypeError('Code must be a string');
    this._code = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
