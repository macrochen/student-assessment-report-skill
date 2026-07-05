import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def convert_html_to_single_page_pdf(html_path):
    if not os.path.exists(html_path):
        print(f"Error: File not found at {html_path}")
        sys.exit(1)
        
    pdf_path = html_path.replace('.html', '.pdf')
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        file_url = f"file://{os.path.abspath(html_path)}"
        print(f"Loading {file_url}...")
        
        await page.goto(file_url)
        
        # Wait for Chart.js and fonts to render
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2000)
        
        # Emulate print media to get accurate layout height
        await page.emulate_media(media="print")
        
        # Get content dimensions
        dimensions = await page.evaluate("""() => {
            return {
                width: document.documentElement.scrollWidth || document.body.scrollWidth,
                height: document.documentElement.scrollHeight || document.body.scrollHeight
            }
        }""")
        
        target_width = max(1100, dimensions["width"])
        target_height = dimensions["height"] + 100
        print(f"Measured Print Dimensions: width={target_width}, height={target_height}")
        
        # Inject @page CSS to force the page size and avoid pagination breaks
        style_content = f"""
        @page {{
            size: {target_width}px {target_height}px !important;
            margin: 0 !important;
        }}
        html, body {{
            height: {target_height}px !important;
            width: {target_width}px !important;
            margin: 0 !important;
            padding: 0 !important;
        }}
        * {{
            page-break-inside: avoid !important;
            page-break-before: avoid !important;
            page-break-after: avoid !important;
        }}
        """
        await page.add_style_tag(content=style_content)
        
        # Generate PDF
        await page.pdf(
            path=pdf_path,
            prefer_css_page_size=True,
            print_background=True,
            display_header_footer=False,
            page_ranges="1"
        )
        print(f"Single-page PDF successfully saved to: {pdf_path}")
        
        await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python html_to_pdf.py <path_to_html_file>")
        sys.exit(1)
        
    html_path = sys.argv[1]
    asyncio.run(convert_html_to_single_page_pdf(html_path))
