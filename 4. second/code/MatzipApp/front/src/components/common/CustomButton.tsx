import React, {ReactNode} from 'react';
import {
  Pressable,
  StyleSheet,
  Text,
  PressableProps,
  Dimensions,
  View,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import {colors} from '../../constants';
import useThemeStore from '@/store/useThemeStore';
import {ThemeMode} from '@/types';

interface CustomButtonProps extends PressableProps {
  label: string;
  variant?: 'filled' | 'outlined';
  size?: 'large' | 'medium';
  inValid?: boolean;
  style?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
  icon?: ReactNode;
}

// 커스텀 버튼에서 직접 onPress를 넣지 말고 PressableProps를 가져와서 이 타입을 확장하겠다.
// -> 이렇게 하면 Pressable이 제공하는 onPress나 onBlur와 같은 기본적인 프롭스들을 일일이 추가하지 않고 한 번에 넘겨줄 수 있다.

// 기기의 높이 가져오기 (안드로이드의 경우 screen은 상태표시줄 포함한 높이, window는 상태표시줄 포함 x한 높이)
// 기기의 높이에 따라 버튼의 크기를 달리 해줄 것 (체감이 틀리므로)
const deviceHeight = Dimensions.get('screen').height;
function CustomButton({
  label,
  variant = 'filled',
  size = 'large',
  inValid = false,
  style = null,
  textStyle = null,
  icon = null,
  ...props
}: CustomButtonProps) {
  const {theme} = useThemeStore();
  const styles = styling(theme);
  return (
    // Pressable: 버튼 컴퍼넌트와 비슷하지만 버튼을 눌렀을 때를 감지해서 스타일 적용 easy
    <Pressable
      disabled={inValid}
      style={({pressed}) => [
        styles.container,
        pressed ? styles[`${variant}Pressed`] : styles[variant],
        inValid && styles.inValid,
        style,
      ]}
      {...props}>
      <View style={styles[size]}>
        {icon}
        <Text style={[styles.text, styles[`${variant}Text`], textStyle]}>
          {label}
        </Text>
      </View>
    </Pressable>
  );
}

const styling = (theme: ThemeMode) =>
  StyleSheet.create({
    container: {
      borderRadius: 3,
      flexDirection: 'row',
      justifyContent: 'center',
    },
    inValid: {
      opacity: 0.5,
    },
    filled: {
      backgroundColor: colors[theme].PINK_700,
    },
    outlined: {
      borderColor: colors[theme].PINK_700,
      borderWidth: 1,
    },
    filledPressed: {
      backgroundColor: colors[theme].PINK_500,
    },
    outlinedPressed: {
      borderColor: colors[theme].PINK_700,
      borderWidth: 1,
      opacity: 0.5,
    },
    large: {
      width: '100%',
      paddingVertical: deviceHeight > 700 ? 15 : 10,
      alignItems: 'center',
      flexDirection: 'row',
      justifyContent: 'center',
      gap: 5,
    },
    medium: {
      width: '50%',
      paddingVertical: deviceHeight > 700 ? 12 : 8,
      alignItems: 'center',
      flexDirection: 'row',
      justifyContent: 'center',
      gap: 5,
    },
    text: {
      fontSize: 16,
      fontWeight: '700',
    },
    filledText: {
      color: colors[theme].WHITE,
    },
    outlinedText: {
      color: colors[theme].PINK_700,
    },
  });
export default CustomButton;
