# miyamoFileNodeFix.py  

## 出来ること  
* 選択した file / place2dTexture（以下p2d）ノードのコネクションをまとめることが出来ます。  
* fileノードはいくつでも、p2dノードは最初に選んだ1つだけに実行されます。  
* p2dノードが選択されていないと、p2dノードを新規作成しそれにつなぎなおします。  
* そのほかのノードを選択しても無視されるので、処理は影響しません。  

（！）接続しなおすアトリビュートは変更できません。  
（！）古いp2dノードは削除されませんが、p2dノードのアトリビュートを変更してる場合は確認することをおすすめします。  

### 使い方  
以下のコードを書いてください  

    import miyamoFileNodeFix 
    miyamoFileNodeFix.main()  
