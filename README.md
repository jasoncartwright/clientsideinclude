# Client Side Include (CSI)
Uses JavaScript to unobtrusively fill an HTML element with the contents of another URL.

## Usage
Include [csi.js](https://github.com/jasoncartwright/clientsideinclude/blob/main/csi.js) anywhere in your HTML...

<code><script src="csi.js" defer></script></code>

Put a URL in the <code>data-include</code> attribute to any element to have it filled with the HTML returned by the URL...

<code>&lt;p data-include=&quot;/path/to/more/content.html&quot;&gt;&lt;/p&gt;</code>

## Example
On https://www.givefood.org.uk the page is cached for up to hours, but contains...

<code><script src="csi.js" defer></script></code>

<code>&lt;p data-include=&quot;/frag/last_updated/&quot;&gt;&lt;/p&gt;</code>

The URL /frag/last_updated/ isn't cached and returns HTML that changes up to every minute.
