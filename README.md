# sample codes using tslearn.
- Purpose: clustering for waveform data or time series data.<br>
- tslearn is one of the Machine Learning libraries based on python.<br>
- tslearn: https://github.com/rtavenar/tslearn

# In Japanese.
- KShapeのアルゴリズムを用いて，サンプルデータに対して波形のクラスタリングを実施しています．
- アルゴリズムには，引数としてクラスタ数を与える必要があります．
    - 今回は事前にデータを確認して，2クラスだとわかっているので，`n_clusters=2`としています．
- クラスタ数については，いくつか確認する方法がありますが，今回はエルボー法を用いて確認しています．
    - 他には，以下の方法があります．
        - BIC・AIC
        - GAP法
        - シルエット法
        - エルボー法
