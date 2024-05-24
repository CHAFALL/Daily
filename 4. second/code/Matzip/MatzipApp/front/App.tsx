import {NavigationContainer} from '@react-navigation/native';
import React from 'react';
import RootNavigator from './src/navigations/root/RootNavigator';

function App() {
  return (
    <NavigationContainer>
      <RootNavigator />
    </NavigationContainer>
  );
}

export default App;

// const [name, setName] = useState('');

// // 리액트 네이티브의 텍스트 인춧은 event.target을 사용할 필요없이 props에 바로 텍스트가 담김
// const handleChangeInput = (text: string) => {
//   console.log(text);
//   setName(text);
// };
