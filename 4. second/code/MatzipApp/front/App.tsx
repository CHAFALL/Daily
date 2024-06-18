import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {QueryClientProvider} from '@tanstack/react-query';
import Toast, {
  BaseToast,
  BaseToastProps,
  ErrorToast,
} from 'react-native-toast-message';

import RootNavigator from './src/navigations/root/RootNavigator';
import queryClient from './src/api/queryClient';
import {colors} from '@/constants';
import {StatusBar} from 'react-native';
import useThemeStorage from '@/hooks/useThemeStorage';

const toastConfig = {
  success: (props: BaseToastProps) => (
    <BaseToast
      {...props}
      style={{borderLeftColor: colors['light'].BLUE_500}}
      text1Style={{
        fontSize: 14,
      }}
      text2Style={{
        fontSize: 12,
      }}
    />
  ),
  error: (props: BaseToastProps) => (
    <ErrorToast
      {...props}
      style={{borderLeftColor: colors['light'].RED_500}}
      text1Style={{
        fontSize: 14,
      }}
      text2Style={{
        fontSize: 12,
      }}
    />
  ),
};

function App() {
  const {theme} = useThemeStorage();

  return (
    <QueryClientProvider client={queryClient}>
      <StatusBar
        barStyle={theme === 'light' ? 'dark-content' : 'light-content'}
      />
      <NavigationContainer>
        <RootNavigator />
        <Toast config={toastConfig} />
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

// 만약에 토스트 메세지를 직접 구현하실 분들은 이렇게 앱 최상단에 구현한 컴포넌트를 추가한 뒤에 Zustand를 이용해서 메세지를 키도 끄는 상태를 전역적으로 관리해주면 된다. (약간 유니티에서 해본 느낌)
// 그리고 스냅바가 표시되는 애니메이션은 React Native의 Animated를 이용
