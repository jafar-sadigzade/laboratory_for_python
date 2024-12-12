import re
import webbrowser
import os
import argparse


# 1. Read the log file and extract URLs using regex
def extract_urls(log_filename):
    if not os.path.isfile(log_filename):
        print(f"Error: File '{log_filename}' not found.")
        return []

    try:
        with open(log_filename, 'r', encoding='utf-8') as file:
            log_data = file.read()

        # Refined regex pattern to capture most URLs
        url_pattern = r'https?://(?:www\.)?[-\w]+(?:\.[\w]+)+(?:/[\w\-.?=&]*)?'
        urls = re.findall(url_pattern, log_data)
        return urls

    except Exception as e:
        print(f"Error reading file: {e}")
        return []


# 2. Check URLs for suspicious keywords
def filter_suspicious_urls(urls, keywords):
    flagged_urls = [url for url in urls if any(keyword in url.lower() for keyword in keywords)]
    return flagged_urls


# 3. Log flagged URLs to a file
def log_flagged_urls(flagged_urls, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for url in flagged_urls:
                file.write(url + '\n')
        print(f"Flagged URLs logged to '{output_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


# 4. Prompt the student to open flagged URLs
def prompt_open_urls(flagged_urls):
    for url in flagged_urls:
        response = input(f"Do you want to open this URL? {url} (yes/no): ").strip().lower()
        if response == 'yes':
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f"Error opening URL {url}: {e}")


# Main function for CLI
def main():
    parser = argparse.ArgumentParser(description="Extract and flag suspicious URLs from a log file.")
    parser.add_argument("log_filename", help="Path to the log file to be analyzed.")
    parser.add_argument("-o", "--output", default="suspicious_urls.txt", help="Output file to save flagged URLs.")
    parser.add_argument("-k", "--keywords", nargs="+", default=['free', 'win', 'prize', 'login', 'account', 'verify'],
                        help="List of keywords to flag URLs as suspicious.")
    parser.add_argument("--open", action="store_true", help="Prompt to open flagged URLs in the web browser.")

    args = parser.parse_args()

    # Extract URLs from the provided log file
    urls = extract_urls(args.log_filename)
    if not urls:
        print("No URLs found in the log file.")
        return

    # Filter for suspicious URLs based on provided keywords
    flagged_urls = filter_suspicious_urls(urls, args.keywords)
    if flagged_urls:
        print(f"Flagged URLs found: {len(flagged_urls)}")

        # Log flagged URLs to the specified output file
        log_flagged_urls(flagged_urls, args.output)

        # Prompt to open flagged URLs if the --open flag is set
        if args.open:
            prompt_open_urls(flagged_urls)
    else:
        print("No suspicious URLs detected.")


if __name__ == "__main__":
    main()
