# Client Side Include
Uses JavaScript to obtrusively fill an HTML element with the contents of another URL.

## Usage
Include [csi.js](https://github.com/jasoncartwright/clientsideinclude/blob/main/csi.js) anywhere in your HTML...

<code><script src="csi.js" defer></script></code>

Add the <code>data-csi</code> attribute to any element to have it filled with the HTML returned by the URL...

<code>&lt;p data-csi=&quot;/path/to/more/html/&quot;&gt;&lt;/p&gt;</code>

## Example
On https://www.givefood.org.uk the page is cached, but contains...

<code><script src="csi.js" defer></script></code>

<code>&lt;p data-csi=&quot;/frag/lastupdated/&quot;&gt;&lt;/p&gt;</code>

The URL /frag/lastupdates/ isn't cached and returns HTML that changes up to every minute.
