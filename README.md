# QA Automation Practice Samples

Existing introductory UI and API testing samples using Python, Playwright, pytest, and Requests. These supplement my manual QA and application-troubleshooting portfolio. AI-assisted development supported scripting and debugging.

## Available evidence

| Sample | Source | Existing screenshot evidence |
| --- | --- | --- |
| Practice-form submission | [Python script](Test_fill_practice_form/test_fill_practice_form.py) | [Recorded run](Test_fill_practice_form/Test_fill_practice_form.png) |
| Add to cart | [Python script](test_add_to_cart/test_add_to_cart.py) | [Recorded run](test_add_to_cart/test_add_to_cart.png) |
| ReqRes GET users | [Python script](test_api_reqres/test_api_reqres.py) | [Recorded run](test_api_reqres/test_api_reqres.png) |
| Elements navigation | [Python script](test_elements_navigation/test_elements_navigation.py) | [Recorded run](test_elements_navigation/test_elements_navigation.png) |
| OrangeHRM login | [Python script](test_orangehrm_login/test_orangehrm_login.py) | [Recorded run](test_orangehrm_login/test_orangehrm_login.png) |
| RESTful Booker authentication | [Python script](test_restful_booker_auth/test_restful_booker_auth.py) | [Recorded run](test_restful_booker_auth/test_restful_booker_auth.png) |
| SauceDemo login | Source not uploaded; screenshots only | [Cursor](login_test_passed/login_test_passed_Cursor.png), [VS Code](login_test_passed/login_test_passed_VS_Code.png) |
| Broken-image diagnostic | Source not uploaded; screenshots only | [Recorded run](test_broken_images/test_broken_images.png) |

Six scripts are available. The two screenshot-only examples do not have downloadable source and are not presented as runnable repository tests. The image-diagnostic screenshot logs loading results without assertions: its pytest pass shows execution completed, not that image behavior met a tested expectation.

The practice-form script checks a successful submission; it does not demonstrate invalid-input or boundary-value coverage. The ReqRes sample checks a GET response, not authentication. RESTful Booker is the API authentication example.

## Running the uploaded samples

From the repository root, with Python and pip available:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install pytest pytest-playwright requests
python -m playwright install chromium
python -m pytest Test_fill_practice_form/test_fill_practice_form.py
```

Replace the final path to run another uploaded script. The practice-form script has an existing custom `playwright` marker that can produce a pytest warning; its recorded screenshot includes that warning.

These samples depend on public demo services, whose interfaces and access requirements can change. Screenshots record earlier runs, not a guarantee that all scripts pass today. No new full-suite run is claimed, no recorded results were changed, and no original dates were updated.

## Related manual QA work

- [Tic for Tot reset investigation](https://github.com/JustinHatch/TicTacToe-QA-BugFix)
- [Contact-form validation](https://github.com/JustinHatch/Broken-Contact-Form-Validation)
- [Gallery image investigation](https://github.com/JustinHatch/Broken-Image-in-Gallery-File-Not-Loading)
- [Training and course certificates](certifications/README.md)

This repository demonstrates portfolio practice and introductory automation skills, not professional QA employment.
