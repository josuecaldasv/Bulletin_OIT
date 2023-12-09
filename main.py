import json
import os


def load_news_data( folder_path ):
    
    news_data = []
    
    for filename in os.listdir( folder_path ):
        if filename.endswith( '.json' ) :
            file_path = os.path.join( folder_path, filename )
            with open( file_path, 'r', encoding = 'utf-8' ) as file:
                news_data.append( json.load( file ) )
    return news_data


def generate_newsletter_html( template_path, news_data ):
    
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()
    
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

    return template.replace("<!-- Aquí se insertarán los artículos de noticias -->", news_items_html )



def main():
    data_folder = 'data'
    template_path = 'template.html'
    output_path = 'sample_bulletin.html'

    news_data = load_news_data(data_folder)
    newsletter_html = generate_newsletter_html(template_path, news_data)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write( newsletter_html )

    print("Boletín generado con éxito.")

if __name__ == "__main__":
    main()