import json
import os

def load_news_data( folder_path ):
    
    """
    Objective:
        - Load news data from JSON files in a specified directory.
    
    Input:
        - folder_path: Path to the directory containing JSON files.
    
    Output:
        - List of dictionaries, where each dictionary contains data for one news item.
    """
    
    news_data = []
    
    for filename in os.listdir( folder_path ):
        if filename.endswith( '.json' ) :
            file_path = os.path.join( folder_path, filename )
            with open( file_path, 'r', encoding = 'utf-8' ) as file:
                news_data.append( json.load( file ) )
    return news_data



def generate_newsletter_html( template_path, news_data ):
    
    """
    Objective:
        - Generate HTML code for a newsletter using a template and news data.
    
    Input:
        - template_path: Path to the HTML template file.
        - news_data: List of news item dictionaries.
    
    Output:
        - A string containing the complete HTML code for the newsletter.
    """
    
    with open( template_path, 'r', encoding = 'utf-8' ) as file:
        template = file.read()
    
    news_items_html = ""

    for news in news_data:
        news_item_html = f"""
        <div class="news-item">
            <img src="{ news[ 'images' ][ 0 ] }" class="news-image">
            <div class="news-content">
                <div class="news-title">{ news[ 'title' ] }</div>
                <div class="news-summary">{news[ 'summary' ] }</div>
                <a href="{ news[ 'actual_link' ] }" class="news-link">Leer más</a>
            </div>
        </div>
        """
        news_items_html += news_item_html

    return template.replace( "<!-- Aquí se insertarán los artículos de noticias -->", news_items_html )


def main():

    """
    Objective:
        - Main function to orchestrate the newsletter generation process.
    
    Process:
        - Load news data, generate newsletter HTML, and save it to a file.
    """
    
    data_folder   = 'data'
    template_path = 'template_2.html'
    output_path   = 'sample_bulletin.html'

    news_data       = load_news_data(data_folder)
    newsletter_html = generate_newsletter_html(template_path, news_data)

    with open( output_path, 'w', encoding = 'utf-8' ) as file:
        file.write( newsletter_html )

    print( "Boletín generado con éxito." )
    

if __name__ == "__main__":
    main()