import {useEffect, useRef, useState} from 'react';
import {AppState} from 'react-native';

function useAppState() {
  const appState = useRef(AppState.currentState);
  const [appStateVisible, setAppStateVisible] = useState(appState.current);

  // 사용자가 허용을 했다가 앱으로 다시 돌아왔다는 상태 값
  const [isComeback, setIscomeback] = useState(false);

  useEffect(() => {
    const subscription = AppState.addEventListener('change', nextAppState => {
      if (
        appState.current.match(/inactive|background/) &&
        nextAppState === 'active'
      ) {
        setIscomeback(true);
      }

      if (appState.current.match(/active/) && nextAppState === 'background') {
        setIscomeback(false);
      }
      appState.current = nextAppState;
      setAppStateVisible(appState.current);
    });

    return () => {
      subscription.remove();
    };
  }, []);

  return {isComeback, appStateVisible};
}

export default useAppState;
