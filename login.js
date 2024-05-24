const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const usernames = process.env.USERNAMES.split(',');
  const passwords = process.env.PASSWORDS.split(',');

  for (let i = 0; i < usernames.length; i++) {
    await page.goto('https://app.koyeb.com/login');
    await page.fill('input[name="email"]', usernames[i]);
    await page.fill('input[name="password"]', passwords[i]);
    await page.click('button[type="submit"]');
    await page.waitForNavigation();

    console.log(`用户 ${usernames[i]} 登录成功！`);
  }

  await browser.close();
})();
