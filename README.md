# Client Side Include (CSI)
Uses JavaScript to unobtrusively fill an HTML element with the contents of another URL.

## Usage
Include csi.min.js anywhere in your HTML...

<code><script src="https://jasoncartwright.github.io/clientsideinclude/csi.min.js" defer></script></code>

Put a URL in the <code>data-include</code> attribute to any element to have it filled with the HTML returned by the URL...

<code>&lt;p data-include=&quot;/path/to/more/content.html&quot;&gt;&lt;/p&gt;</code>

You can also add <code>data-update</code> containing the number of seconds that the include should be reloaded.

<code>&lt;p data-include=&quot;/path/to/some/livecontent.html&quot; data-update=&quot;60&quot;&gt;&lt;/p&gt;</code>

You can also add <code>data-stop-when</code> to stop the <code>data-update</code> polling when the trimmed included content equals the specified value (the fetched response text is trimmed before comparison, so leading and trailing whitespace in the response is ignored).

<code>&lt;p data-include=&quot;/path/to/some/livecontent.html&quot; data-update=&quot;60&quot; data-stop-when=&quot;0&quot;&gt;&lt;/p&gt;</code>

## Example
Code: https://github.com/jasoncartwright/clientsideinclude/blob/main/example.html

Preview: https://htmlpreview.github.io/?https://github.com/jasoncartwright/clientsideinclude/blob/main/example.html
