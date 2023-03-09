# LinkedIn Job Application Automation
<p>This is a Python script that automates job applications on LinkedIn. The script logs into a LinkedIn account, navigates to a job search page, and applies to all the jobs on the page. The application was created as part of the 100 Days of Code - The Complete Python Pro Bootcamp course challenge.</p>Prerequisites
<p>To run the script, you will need:</p>
<ul>
 <li>Python 3.6 or higher installed on your computer</li>
 <li>Chrome browser installed on your computer</li>
 <li>ChromeDriver installed on your computer and added to your system PATH</li>
 <li>A LinkedIn account with login credentials</li>
</ul>Installation
<ol>
 <li>Clone the repository or download the source code as a ZIP file.</li>
 <li>Navigate to the project directory in your terminal.</li>
 <li>Install the required Python libraries by running <code>pip install -r requirements.txt</code> in your terminal.</li>
</ol>Usage
<ol>
 <li>Set your LinkedIn account credentials in a <code>.env</code> file in the project directory. For example:<pre><code>USER_NAME=your_username
PASSWORD=your_password
</code></pre></li>
 <li>Run the script by running <code>python main.py</code> in your terminal.</li>
 <li>The script will log into your LinkedIn account, navigate to a job search page, and apply to all the jobs on the page.</li>
</ol>Customization
<p>The script is currently set to search for Python web developer jobs in Poland. If you want to customize the job search, you can modify the <code>JOB_SEARCH_URL</code> variable in the <code>LinkedInJobApply</code> class.</p>Acknowledgments
<ul>
 <li>This script was developed using the Selenium WebDriver library.</li>
 <li>The <code>.env</code> file is loaded using the <code>dotenv</code> library.</li>
 <li>This README was created with the help of a <a href="https://github.com/othneildrew/Best-README-Template" rel="nofollow">README template</a> by <a href="https://github.com/othneildrew" rel="nofollow">Othneil Drew</a>.</li>
</ul>
