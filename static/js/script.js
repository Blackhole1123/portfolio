class Header extends HTMLElement{
  constructor(){
    super();
  }
  connectedCallback(){
    this.innerHTML = `
<p style="text-align:center;">™ and © 2022, Rishaan Desai</p>
    `
  }
}
customElements.define('copyright-footer', Header);