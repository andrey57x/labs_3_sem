namespace Files
{
    partial class Form
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            ChooseFile = new Button();
            Time1 = new TextBox();
            SearchBox = new TextBox();
            SearchButton = new Button();
            listBox = new ListBox();
            Time2 = new TextBox();
            SuspendLayout();
            // 
            // ChooseFile
            // 
            ChooseFile.Cursor = Cursors.AppStarting;
            ChooseFile.FlatStyle = FlatStyle.System;
            ChooseFile.Location = new Point(674, 58);
            ChooseFile.Name = "ChooseFile";
            ChooseFile.Size = new Size(75, 25);
            ChooseFile.TabIndex = 0;
            ChooseFile.Text = "Choose File";
            ChooseFile.TextImageRelation = TextImageRelation.ImageBeforeText;
            ChooseFile.UseVisualStyleBackColor = true;
            // 
            // Time1
            // 
            Time1.Location = new Point(662, 29);
            Time1.Name = "Time1";
            Time1.Size = new Size(100, 23);
            Time1.TabIndex = 1;
            // 
            // SearchBox
            // 
            SearchBox.Location = new Point(40, 13);
            SearchBox.Multiline = true;
            SearchBox.Name = "SearchBox";
            SearchBox.Size = new Size(207, 54);
            SearchBox.TabIndex = 2;
            // 
            // SearchButton
            // 
            SearchButton.Location = new Point(253, 28);
            SearchButton.Name = "SearchButton";
            SearchButton.Size = new Size(75, 23);
            SearchButton.TabIndex = 3;
            SearchButton.Text = "Search";
            SearchButton.UseVisualStyleBackColor = true;
            // 
            // listBox
            // 
            listBox.FormattingEnabled = true;
            listBox.ItemHeight = 15;
            listBox.Location = new Point(40, 92);
            listBox.Name = "listBox";
            listBox.Size = new Size(288, 289);
            listBox.TabIndex = 4;
            // 
            // Time2
            // 
            Time2.Location = new Point(345, 28);
            Time2.Name = "Time2";
            Time2.Size = new Size(100, 23);
            Time2.TabIndex = 5;
            // 
            // Form
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(800, 450);
            Controls.Add(Time2);
            Controls.Add(listBox);
            Controls.Add(SearchButton);
            Controls.Add(SearchBox);
            Controls.Add(Time1);
            Controls.Add(ChooseFile);
            Name = "Form";
            Text = "Form";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button ChooseFile;
        private TextBox Time1;
        private TextBox SearchBox;
        private Button SearchButton;
        private ListBox listBox;
        private TextBox Time2;
    }
}
