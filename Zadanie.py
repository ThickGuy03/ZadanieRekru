import requests

# Klucz API OpenAI (wprowadz swój klucz)
API_KEY = ""


def fetch_article_content():
    """Tresc artykulu."""
    content = """
    Sztuczna inteligencja: wptyw i wyzwania

    Sztuczna inteligencja to dziedzina nauki i technologii zajmujaca sie tworzeniem maszyn i programów zdolnych do wykonywania zadaz wymagajacych ludzkiej inteligencji, takich jak uczenie sie, rozumienie jezyka naturalnego i podejmowanie decyzji. AI stala sie integralna czescia naszego codziennego zycia, od asystentów glosowych w smartfonach, jak Siri czy Google Assistant, po systemy rekomendacyjne na platformach streamingowych, takich jak Netflix czy Spotify. Wspiera nas w planowaniu tras, automatyzacji domowych urzadzen oraz w komunikacji. Obecnie jest o niej bardzo glosno chociazby za sprawa duzych modeli jezykowych, jak ChatGPT.

    Rozwój uczenia maszynowego i glebokiego uczenia umozliwil tworzenie zaawansowanych modeli, które potrafia samodzielnie rozwiazywac skomplikowane problemy. Sieci neuronowe analizuja ogromne ilosci danych w obszarach takich jak rozpoznawanie obrazów czy przetwarzanie jezyka naturalnego. Dzieki temu AI nie tylko przetwarza dane, ale takze podejmuje decyzje, wczesniej zarezerwowane dla ludzi.

    Wyzwania etyczne i spoleczne

    Kluczowym wyzwaniem jest zapewnienie etycznego i odpowiedzialnego rozwoju AI. Nalezy zwracac uwage na uprzedzenia w danych treningowych, które moga prowadzic do dyskryminacji, oraz na wplyw AI na prywatnosc i nierównosci spoleczne. Wazne jest opracowanie ram etycznych i mechanizmów nadzoru regulujacych rozwój i wdrazanie AI, a takze wlaczanie róznych grup spolecznych w ten proces. Transparentnosc dzialan firm i instytucji moze pomóc w budowaniu zaufania do technologii.

    Badacze pracuja nad rozwiazaniami umozliwiajacymi harmonijne wspólistnienie ludzi i AI, koncentrujac sie na tworzeniu systemów wspierajacych czlowieka, a nie go zastepujacych. Istotne jest opracowywanie mechanizmów wspólpracy miedzy czlowiekiem a maszyna, co sprzyja synergii i skutecznej komunikacji.

    Automatyzacja i przyszlosc rynku pracy

    Automatyzacja procesów dzieki AI przynosi korzysci w postaci zwiekszonej efektywnosci i redukcji kosztów. Jednak istnieja obawy dotyczace wplywu na rynek pracy i potencjalnego zastapienia ludzi przez maszyny. Kluczowe jest przemyslane podejscie do transformacji rynku pracy, inwestycja w edukacje i przekwalifikowanie pracowników, aby mogli oni znalezc nowe role w gospodarce przyszlosci.

    Specjalisci powinni byc gotowi na ciagle doskonalenie swoich umiejetnosci, uczac sie m.in. zasad dzialania algorytmów AI. Przyszlosc pracy bedzie wymagac nie tylko umiejetnosci technicznych, ale takze kompetencji miekkich, takich jak kreatywnosc i zdolnosc rozwiazywania problemów.

    Nasza zdolnosc do adaptacji i innowacji zdecyduje o tym, jak AI wplynie na przyszlosc ludzkosci. Wspólnie mozemy ksztaltowac te przyszlosc, wykorzystujac AI dla dobra wszystkich.
    """
    return content


def generate_html_content(article_content, prompt):
    """Przekazuje artykul i prompt do OpenAI w celu wygenerowania kodu HTML."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",  # Mozesz uzyc innego modelu, np. gpt-3.5-turbo
        "messages": [
            {
                "role": "system",
                "content": "Zwróc odpowiedni kod HTML dla tresci artykulu."
            },
            {
                "role": "user",
                "content": f"{prompt}\n\nTresc artykulu:\n{article_content}"
            }
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_json = response.json()

    # Wydobycie wygenerowanego kodu HTML
    html_content = response_json["choices"][0]["message"]["content"]
    return html_content


def save_html_to_file(html_content, filename="artykul.html"):
    """Zapisuje wygenerowany kod HTML do pliku artykul.html."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    # Prompt do OpenAI
    prompt = (
        "Przetlumacz artykul na HTML, stosujac odpowiednie tagi strukturalne, "
        "uzywajac <img> z atrybutem src='image_placeholder.jpg' dla proponowanych miejsc na grafiki. "
        "Dodaj atrybut alt z dokladnym promptem do generowania grafiki oraz podpisy pod grafikami."
    )

    # Krok 1: Wczytaj tresc artykulu
    article_content = fetch_article_content()

    # Krok 2: Wygeneruj HTML za pomoca OpenAI
    html_content = generate_html_content(article_content, prompt)

    # Krok 3: Zapisz HTML do pliku
    save_html_to_file(html_content)

    print("Plik artykul.html zostal wygenerowany.")


if __name__ == "__main__":
    main()
