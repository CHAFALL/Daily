import AuthStackNavigator from '../stack/AuthStackNavigator';
import MainDrawNavigator from '../drawer/MainDrawerNavigator';

function RootNavigator() {
  const isLoggedIn = false;

  return <>{isLoggedIn ? <MainDrawNavigator /> : <AuthStackNavigator />}</>;
}

export default RootNavigator;
