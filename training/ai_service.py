import os
import openai
from dotenv import load_dotenv
from .models import WorkoutSession, ExerciseInSession


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_training_advice(workout_plan, user_profile):
    sessions = WorkoutSession.objects.filter(workout_plan=workout_plan).order_by('date')
    prompt = f"""Jesteś doświadczonym trenerem personalnym pomagającym trenować zdrowo i bezpiecznie.
                    Plan treningowy trenującego:
                    - Nazwa:{workout_plan.name}
                    - Opis: {workout_plan.description if workout_plan.description else 'Brak opisu'}
                    
                    Profil trenującego:
                    - Wzrost: {user_profile.height} centymetrów
                    - Waga: {user_profile.weight} kilogramów
                    - Doświadczenie treningowe: {user_profile.experience_in_months} miesięcy
                    - Wiek: {user_profile.age} lat
                    - Dodatkowe informacje: {user_profile.additional_info if user_profile.additional_info else 'Brak informacji'}
                    """

    prompt += "\nSesje treningowe i ćwiczenia w sesjach:"
    if sessions.exists():
        for session in sessions:
            prompt += f"""\nNazwa sesji: {session.name}
                            - Data: {session.date}
                            - Status: {session.get_status_display()}
                            - Notatki trenującego: {session.note if session.note else 'Brak notatek'}
                            """
            exercises_in_session = ExerciseInSession.objects.filter(workout_session=session)
            if exercises_in_session.exists():
                for exercise in exercises_in_session:
                    prompt += f"""\nNazwa ćwiczenia: {exercise.exercise.name}
                                    - Liczba serii: {exercise.sets}
                                    - Liczba powtórzeń w serii: {exercise.repetitions}
                                    - Ciężar: {exercise.weight} kilogramów
                                    """
            else:
                prompt += ("""\nBrak ćwiczeń w tej sesji, zaproponuj trenującemu ćwiczenia jakie może dodać do tej sesji,
                                z licbą serii, powtórzeń i ciężarem, oraz krótką poradą""")
    else:
        prompt += """\nTrenujący nie dodał jeszcze żadnych sesji treningowych do tego planu, zaproponuj trenującemu sesje treningowe, 
                       które może dodać do tego planu z nazwą i datą, a do każdej zaproponowanej sesji zaproponuj trenującemu ćwiczenia,
                       jakie może dodać do tej sesji, z liczbą serii, powtórzeń i ciężarem)"""

    prompt += """\nNa podstawie powyższych danych zaproponuj:
                   - 2–3 zdrowe i konkretne porady treningowe.
                   - Dodatkowo zweryfikuj czy trenujący rozwija się na podstawie dat sesji treningowych oraz ćwiczeń w danej sesji,
                     porównując dane ćwiczeń w danej sesji z danymi innych sesji czyli seriami, powtórzeniami i ciężarem, 
                     weź również pod uwagę specyfikę i charakter planu treningowego, sesji treningowych i ćwiczeń, aby były kompatybilne i sensowne.
                   - Jeżeli trenujący się nie rozwija zaproponuj zmiany, które pozwolą mu osiągnąć progres, dbając o jego zdrowie.
                   - Jeżeli trenujący nie rozpoczął jeszcze realizacji planu, możesz zaproponować od czego warto zacząć. 
                   - Unikaj ekstremalnych zaleceń, skup się na praktycznych wskazówkach: np. jak ułożyć pierwszą sesję, jak dobrać ćwiczenia, 
                     jak dostosować obciążenie, jak uniknąć kontuzji.
                   """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Jesteś pomocnym trenerem personalnym."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=700,
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"Wystąpił błąd: {error}"
