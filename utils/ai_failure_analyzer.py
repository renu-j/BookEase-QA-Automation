
def analyze_failure(test_name, error_message):
    """
    Analyze a test failure and provide a concise
    troubleshooting suggestion.
    """

    error = error_message.lower()

    if "timeoutexception" in error:
        analysis = (
            "Likely cause: The expected element was not found "
            "or did not become available within the configured "
            "wait time.\n\n"
            "Suggested action: Check the locator, page state, "
            "and synchronization/wait conditions."
        )

    elif "nosuchelementexception" in error:
        analysis = (
            "Likely cause: Selenium could not find the expected "
            "element in the current DOM.\n\n"
            "Suggested action: Verify the locator against the "
            "current application DOM."
        )

    elif "assertionerror" in error:
        analysis = (
            "Likely cause: The actual application result did not "
            "match the expected result.\n\n"
            "Suggested action: Review the assertion and compare "
            "the expected result with the actual application behavior."
        )

    elif "typeerror" in error:
        analysis = (
            "Likely cause: Incorrect object usage, constructor "
            "arguments, or method parameters.\n\n"
            "Suggested action: Check the class constructor and "
            "the arguments passed to the method."
        )

    elif "connection" in error:
        analysis = (
            "Likely cause: Application or network connectivity "
            "problem.\n\n"
            "Suggested action: Check whether the application/API "
            "is reachable and available."
        )

    else:
        analysis = (
            "The failure requires further investigation.\n\n"
            "Suggested action: Review the traceback, screenshot, "
            "locator, and application state."
        )

    return (
        "AI FAILURE ANALYSIS\n"
        "===================\n\n"
        f"Test: {test_name}\n\n"
        f"Analysis:\n{analysis}\n"
    )

