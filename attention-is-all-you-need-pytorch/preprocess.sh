
<<<<<<< HEAD
python ../analysis/dataPreprocess.py ../data/kaggle_norm_competition/en_train.csv 3
python ../analysis/dataPreprocess.py ../data/kaggle_norm_competition/en_train.csv 4
python ../analysis/dataPreprocess.py ../data/kaggle_norm_competition/en_test.csv 2

# for l in en de; do for f in data/kaggle_norm_competition/*.$l; do if [[ "$f" != *"test"* ]]; then sed -i "$ d" $f; fi;  done; done
# for l in en de; do for f in data/kaggle_norm_competition/*.$l; do perl tokenizer.perl -a -no-escape -l $l -q  < $f > $f.atok; done; done

=======
>>>>>>> f60d4858ec9e060c082deac46db80435d56cab6a
python preprocess.py -train_src ../data/kaggle_norm_competition/en_train_SRC.txt -train_tgt ../data/kaggle_norm_competition/en_train_DST.txt -valid_src ../data/kaggle_norm_competition/en_val_SRC.txt -valid_tgt ../data/kaggle_norm_competition/en_val_DST.txt -save_data data/kaggle_norm_competition/train_kaggle2transformer.atok.low.pt
