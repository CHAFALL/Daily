import AuthStackNavigator from '../stack/AuthStackNavigator';
import MainDrawNavigator from '../drawer/MainDrawerNavigator';
import useAuth from '@/hooks/queries/useAuth';
import React, {useEffect} from 'react';
import RetryErrorBoundary from '@/components/common/RetryErrorBoundary';
import SplashScreen from 'react-native-splash-screen';

function RootNavigator() {
  const {isLogin, isLoginLoading} = useAuth();

  useEffect(() => {
    if (!isLoginLoading) {
      setTimeout(() => {
        SplashScreen.hide();
      }, 500);
    }
  }, [isLoginLoading]);

  return (
    <RetryErrorBoundary>
      {isLogin ? <MainDrawNavigator /> : <AuthStackNavigator />}
    </RetryErrorBoundary>
  );
}

export default RootNavigator;

// 스플래시 스크린 -> 앱을 실행했을 때 보여주는 시작 화면
