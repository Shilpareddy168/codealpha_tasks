"""
TASK 3: Task Automation with Python Scripts
Complete implementation of all three options
"""

import os
import shutil
import re
import requests


# ============================================================================
# OPTION 1: Move JPG Files
# ============================================================================

def move_jpg_files():
    """Move all .jpg files from source folder to destination folder"""
    
    # Create test folders
    source_folder = "source_images"
    destination_folder = "jpg_images"
    
    # Create folders if they don't exist
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(destination_folder, exist_ok=True)
    
    # Create some sample .jpg files for testing
    sample_files = ["photo1.jpg", "photo2.jpg", "document.txt", "photo3.jpg", "notes.pdf"]
    for filename in sample_files:
        filepath = os.path.join(source_folder, filename)
        with open(filepath, 'w') as f:
            f.write(f"Sample content for {filename}")
    
    print("=" * 60)
    print("OPTION 1: Moving JPG Files")
    print("=" * 60)
    
    # Get all files in source folder
    files = os.listdir(source_folder)
    jpg_count = 0
    
    # Move only .jpg files
    for filename in files:
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}")
            jpg_count += 1
    
    print(f"\nTotal JPG files moved: {jpg_count}")
    print(f"Files remaining in source: {os.listdir(source_folder)}")
    print(f"Files in destination: {os.listdir(destination_folder)}")
    print()


# ============================================================================
# OPTION 2: Extract Email Addresses
# ============================================================================

def extract_emails():
    """Extract all email addresses from a text file"""
    
    input_file = "sample_text.txt"
    output_file = "extracted_emails.txt"
    
    # Create sample text file with email addresses
    sample_text = """
    Hello, please contact us at support@example.com for assistance.
    You can also reach out to sales@company.org or info@business.net.
    
    Our team members:
    - John Doe: john.doe@example.com
    - Jane Smith: jane.smith123@example.co.uk
    - Bob Johnson: bob_johnson@testmail.com
    
    For urgent matters, email emergency@help.io
    Invalid emails: @nodomain.com, notemail@, just.text
    """
    
    with open(input_file, 'w') as f:
        f.write(sample_text)
    
    print("=" * 60)
    print("OPTION 2: Extracting Email Addresses")
    print("=" * 60)
    
    # Read the input file
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Regular expression pattern for email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all email addresses
    emails = re.findall(email_pattern, content)
    
    # Remove duplicates and sort
    unique_emails = sorted(set(emails))
    
    # Save to output file
    with open(output_file, 'w') as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 40 + "\n\n")
        for email in unique_emails:
            f.write(email + "\n")
    
    print(f"Found {len(unique_emails)} unique email address(es):")
    for email in unique_emails:
        print(f"  - {email}")
    
    print(f"\nEmails saved to: {output_file}")
    print()


# ============================================================================
# OPTION 3: Scrape Webpage Title
# ============================================================================

def scrape_webpage_title():
    """Scrape the title of a webpage and save it"""
    
    output_file = "webpage_title.txt"
    
    # Using a reliable public website
    url = "https://www.example.com"
    
    print("=" * 60)
    print("OPTION 3: Scraping Webpage Title")
    print("=" * 60)
    
    try:
        # Make HTTP request
        print(f"Fetching webpage: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Extract title using regex
        title_pattern = r'<title>(.*?)</title>'
        match = re.search(title_pattern, response.text, re.IGNORECASE)
        
        if match:
            title = match.group(1).strip()
            
            # Save to file
            with open(output_file, 'w') as f:
                f.write(f"Webpage Title Scraper\n")
                f.write("=" * 40 + "\n\n")
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n")
                f.write(f"Status Code: {response.status_code}\n")
            
            print(f"Title found: {title}")
            print(f"Title saved to: {output_file}")
        else:
            print("No title found on the webpage")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        print("Note: This requires internet connection")
    
    print()


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main function to run the task automation script"""
    
    print("\n" + "=" * 60)
    print("TASK 3: TASK AUTOMATION WITH PYTHON SCRIPTS")
    print("=" * 60)
    print("\nThis script demonstrates three automation tasks:")
    print("1. Move JPG files from one folder to another")
    print("2. Extract email addresses from a text file")
    print("3. Scrape webpage title and save it")
    print("\n" + "=" * 60 + "\n")
    
    while True:
        print("\nChoose an option:")
        print("1 - Move JPG Files")
        print("2 - Extract Email Addresses")
        print("3 - Scrape Webpage Title")
        print("4 - Run All Tasks")
        print("0 - Exit")
        
        choice = input("\nEnter your choice (0-4): ").strip()
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            move_jpg_files()
            extract_emails()
            scrape_webpage_title()
            print("=" * 60)
            print("All tasks completed!")
            print("=" * 60)
        elif choice == '0':
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()