import json
import os

def load_news_data_from_folder(folder_path):
    """
    Objective:
        Load news data from JSON files within a specified folder.
    
    Input:
        folder_path: String. The path to the folder containing JSON files.
    
    Output:
        List of dictionaries. Each dictionary contains data from one news item.
    """
    news_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                news_data.append(json.load(file))
    return news_data


def load_news_data(base_folder):
    """
    Objective:
        Load news data from multiple subfolders within a base directory, 
        treating each subfolder as a separate news section.
    
    Input:
        base_folder: String. The path to the base directory containing subfolders.
    
    Output:
        Dictionary. Keys are folder names, and values are lists of news data 
        (dictionaries) loaded from each folder.
    """
    sections = {}
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        if os.path.isdir(folder_path):
            sections[folder_name] = load_news_data_from_folder(folder_path)
    return sections


def generate_news_section(section_name, news_data):
    """
    Objective:
        Generate HTML content for a single news section.
    
    Input:
        section_name : String. The name of the news section.
        news_data    : List of dictionaries. Each dictionary contains data for one news item.
    
    Output:
        String. HTML content for the news section.
    """
    
    news_items_html = ""
    for news in news_data:
        news_item_html = f"""
        <div class="news-item">
            <img src="{news['images'][0]}" class="news-image">
            <div class="news-content">
                <div class="news-title">{news['title']}</div>
                <div class="news-summary">{news['summary']}</div>
                <a href="{news['actual_link']}" class="news-link">Leer más</a>
            </div>
        </div>
        """
        news_items_html += news_item_html
    return f"<h2 class='news-title-center'>{section_name}</h2>{news_items_html}"


def generate_newsletter_html(template_path, sections_data):
    """
    Objective:
        Generate the complete HTML for the newsletter using a template and news data.
    
    Input:
        template_path: String. The path to the HTML template file.
        sections_data: Dictionary. Contains news data for each section.
    
    Output:
        String. Complete HTML code for the newsletter.
    """
    
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    all_sections_html = ""
    for section_name, news_data in sections_data.items():
        all_sections_html += generate_news_section(section_name, news_data)

    return template.replace("<!-- Aquí se insertarán los artículos de noticias -->", all_sections_html)


def main():
    """
    Objective:
        Main function to orchestrate the newsletter generation process.
    
    Process:
        Load news data, generate newsletter HTML, and save it to a file.
    """
    data_folder = 'data'
    template_path = 'template_2.html'
    output_path = 'sample_bulletin.html'

    sections_data = load_news_data(data_folder)
    newsletter_html = generate_newsletter_html(template_path, sections_data)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(newsletter_html)

    print("Boletín generado con éxito.")

    
    
if __name__ == "__main__":
    main()