def execute_keyword(page, keyword, target=None, value=None):
    """
    Simple Keyword Action Executor.
    Executes a high-level keyword action (OPEN, CLICK, FILL, SEARCH, ADD_TO_CART, OPEN_CART, LOGOUT)
    using Playwright page commands.
    """
    print(f"\n[Keyword Action]: {keyword} | Target: {target} | Value: {value}")
    
    keyword_upper = keyword.upper()
    
    if keyword_upper == "OPEN":
        url = target or "https://automationexercise.com/"
        page.goto(url, wait_until="domcontentloaded")
    elif keyword_upper == "CLICK":
        page.locator(target).click()
    elif keyword_upper == "FILL":
        page.locator(target).fill(value)
    elif keyword_upper == "SEARCH":
        page.locator("#search_product").fill(value)
        page.locator("#submit_search").click()
    elif keyword_upper == "ADD_TO_CART":
        page.locator(".product-overlay a.add-to-cart, .productinfo a.add-to-cart").first.click()
    elif keyword_upper == "OPEN_CART":
        page.locator(".modal-content a[href='/view_cart']").click()
    elif keyword_upper == "LOGOUT":
        page.locator("a[href='/logout']").click()
    else:
        raise ValueError(f"Unknown keyword action: {keyword}")
