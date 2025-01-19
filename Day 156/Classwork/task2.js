import { useEffect, useState } from 'react';

const App = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState("");

  useEffect(() => {
    console.log("button clicked")
  }, [name]) // [] - დამოკიდებულების მასივი(ჩავწერთ იმ მდგომარეობებს, რომელბზეც იქნება ჩვენი effect ფუნქცია დამოკიდებული)

  // თუ არაფერს გადავცემთ useEffect-ს მეორე არგუმენტად, effect ფუნქცია გაეშვება ნებისმიერი მდგომარეობის შეცვლისას
  // თუ გადავეცით ცარიელი მასივი, effect ფუნქცია გაეშვება მხოლოდ კომპონენტის პირველი დარენდერებისას
  // თუ დამოკიდებულების მასივში ჩავწერეთ მდგომარეობის სახელი, effect ფუნქცია გაეშვება მხოლოდ გადაცემული მდგომარეობის შეცვლისას და არა ნებისმიერის

  const handleChange = ({ target }) => {
    setName(target.value)
  }

  return (
    <>
      <button onClick={() => setCount(prev => prev + 1)}>Clicked times: {count}</button>
      <p>Name: {name}</p>
      <input type="text" value={name} onChange={handleChange} />
    </>
  );
}

export default App;