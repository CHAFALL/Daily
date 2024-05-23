import {NavigationContainer} from '@react-navigation/native';
import React, {useState} from 'react';
import {StyleSheet} from 'react-native';
import AuthStackNavigator from './src/navigation/AuthStackNavigator';

function App() {
  const [name, setName] = useState('');

  // 리액트 네이티브의 텍스트 인춧은 event.target을 사용할 필요없이 props에 바로 텍스트가 담김
  const handleChangeInput = (text: string) => {
    console.log(text);
    setName(text);
  };
  return (
    <NavigationContainer>
      <AuthStackNavigator />
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  input: {
    // 인풋을 꽉 차게
    flex: 1,
    borderWidth: 2,
    borderColor: 'black',
  },
  inputContainer: {
    flex: 1,
    // 기본방향이 col로 되어있음
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;
