# what is URL list out all types of URL ?
  
  # URL (Uniform Resource Locator)

A **URL (Uniform Resource Locator)** is the web address used to locate and access resources on the Internet such as web pages, images, videos, files, and APIs.

## URL Structure

Example:

https://www.example.com/products/index.html?id=101#details

Components:

| Component | Example | Description |
|------------|---------|-------------|
| Protocol (Scheme) | https | Communication protocol |
| Domain Name | www.example.com | Website address |
| Path | /products/index.html | Resource location |
| Query String | ?id=101 | Parameters sent to server |
| Fragment | #details | Section within page |

---

## Types of URLs

### 1. Absolute URL

A complete URL containing:

- Protocol
- Domain Name
- Path

Example:

https://www.example.com/about.html

Characteristics:

- Complete web address
- Works from any location
- Commonly used for external links

Examples:

https://www.google.com/

https://www.example.com/products/mobile.html

https://api.example.com/users/101

or

https://www.tops-int.com/

---

### 2. Relative URL

A URL that specifies the path relative to the current page.

Examples:

https://www.tops-int.com/it-training-rajkot

about.html

products/mobile.html

images/logo.png

Characteristics:

- Does not contain protocol
- Does not contain domain name
- Used within the same website

---

### 3. Root Relative URL

Starts from the website root directory.

Examples:

/about.html

/products/mobile.html

/images/logo.png

---

### 4. Protocol Relative URL

Uses the current page protocol automatically.

Example:

//cdn.example.com/style.css

Note:
This approach is less common today because HTTPS is generally preferred.

---

### 5. Dynamic URL

Generated dynamically using parameters.

Example:

https://example.com/product?id=101

https://example.com/search?q=laptop

---

### 6. Static URL

Represents a fixed page location.

Example:

https://example.com/about-us

https://example.com/contact

---

## Absolute URL vs Relative URL

### Absolute URL

Current Page:
Any page

Link:

https://www.example.com/images/logo.png

Result:

Always points to the same resource.

---

### Relative URL

Current Page:

https://www.example.com/products/

Link:

mobile.html

Result:

https://www.example.com/products/mobile.html

---

## Examples of Relative URLs

### Same Folder

Current Page:

https://www.example.com/products/

Link:

mobile.html

Result:

https://www.example.com/products/mobile.html

---

### Child Folder

Link:

images/logo.png

Result:

https://www.example.com/products/images/logo.png

---

### Parent Folder

Link:

../index.html

Result:

https://www.example.com/index.html

---

### Root Relative

Link:

/contact.html

Result:

https://www.example.com/contact.html

---

## Common URL Schemes (Protocols)

| Scheme | Purpose |
|----------|---------|
| https:// | Secure websites |
| http:// | Websites |
| ftp:// | File transfer |
| sftp:// | Secure file transfer |
| mailto: | Email links |
| tel: | Phone links |
| file:// | Local files |
| ws:// | WebSocket |
| wss:// | Secure WebSocket |

---

## URL Examples

### Website URL

https://www.example.com

### Image URL

https://www.example.com/images/logo.png

### API URL

https://api.example.com/users

### Email URL

mailto:support@example.com

### Phone URL

tel:+911234567890

---

## Summary

A URL is the address of a resource on the Internet.

Main URL Types:

1. Absolute URL
2. Relative URL
3. Root Relative URL
4. Protocol Relative URL
5. Dynamic URL
6. Static URL

Most websites use:
- HTTPS URLs
- Absolute URLs for external resources
- Relative URLs for internal navigation