#!/bin/bash

sum_of_square() {
  SUM=0
  I=1
  while [ $I -le $1 ]; do
    Q=$((I * I))
    SUM=$((SUM + Q))
    I=$((I + 1))
  done
  echo $SUM
}

sum() {
  SUM=0
  I=1
  while [ $I -le $1 ]; do
    SUM=$((SUM + $I))
    I=$((I + 1))
  done
  R=$(($SUM ** 2))
  echo $R
}

echo "Enter a number:"
read NUMBER

sub() {
  RS=$(sum $NUMBER)
  RSQ=$(sum_of_square $NUMBER)
  R=$((RS - RSQ))
  echo "RESULT: $R"
}

sub
