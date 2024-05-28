import React from 'react';
import {QueryClientProvider} from '@tanstack/react-query';
import {NavigationContainer} from '@react-navigation/native';
import RootNavigator from './src/navigations/root/RootNavigator';
import queryClient from './src/api/queryClient';

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <NavigationContainer>
        <RootNavigator />
      </NavigationContainer>
    </QueryClientProvider>
  );
}

export default App;

// const [name, setName] = useState('');

// // 리액트 네이티브의 텍스트 인춧은 event.target을 사용할 필요없이 props에 바로 텍스트가 담김
// const handleChangeInput = (text: string) => {
//   console.log(text);
//   setName(text);
// };
