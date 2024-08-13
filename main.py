import scraper
import migration

SOURCE = 'https://komiku.id/'

def main():
    data = scraper.scrape_data(SOURCE)
    migration.migrate_data(data)

if __name__ == "__main__":
    main()